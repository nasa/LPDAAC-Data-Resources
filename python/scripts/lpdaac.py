"""
Set of helpful functions for working with LPDAAC Data.

Use below for more info:

python lpdaac.py --help 

python lpdaac.py search --help

"""
#TODO Add provider argument
#TODO Add download function
#TODO Package up
#TODO Write read me

import json
import os
import click
import earthaccess
import geopandas as gpd
from shapely.geometry.polygon import orient

# Custom Search Click Types

class TemporalType(click.ParamType):
    name = "temporal"

    def convert(self, value, param, ctx):
        try:
            parts = value.split("/")
            if len(parts) != 2:
                self.fail("Temporal value must be in 'start/end' format.", param, ctx)
            # (Optional) Further validate the dates/datetimes here.
            return tuple(parts)
        except Exception as e:
            self.fail(f"Error parsing temporal value: {e}", param, ctx)


class BBoxType(click.ParamType):
    name = "bbox"

    def convert(self, value, param, ctx):
        try:
            parts = value.split(",")
            if len(parts) != 4:
                self.fail("Bounding box must have 4 comma-separated values (minLon,minLat,maxLon,maxLat).", param, ctx)
            return tuple(map(float, parts))
        except Exception as e:
            self.fail(f"Error parsing bounding box: {e}", param, ctx)


class PointType(click.ParamType):
    name = "point"

    def convert(self, value, param, ctx):
        try:
            parts = value.split(",")
            if len(parts) != 2:
                self.fail("Point must have 2 comma-separated values (lon,lat).", param, ctx)
            return tuple(map(float, parts))
        except Exception as e:
            self.fail(f"Error parsing point: {e}", param, ctx)

class GeoJSONType(click.ParamType):
    name = "geojson"

    def convert(self, value, param, ctx):
        try:
            # Read the GeoJSON file using GeoPandas
            gdf = gpd.read_file(value)
            if gdf.empty:
                self.fail("GeoJSON file is empty.", param, ctx)

            # Assume the first feature's geometry is the one you need.
            geom = gdf.iloc[0].geometry
            if geom.geom_type != "Polygon":
                self.fail("GeoJSON geometry must be a Polygon.", param, ctx)

            # Orient the polygon so that its exterior ring is counterclockwise.
            oriented = orient(geom, sign=1.0)
            # Extract and return the exterior coordinates as a list of tuples.
            exterior = list(oriented.exterior.coords)
            return exterior

        except Exception as e:
            self.fail(f"Error parsing GeoJSON with geopandas: {e}", param, ctx)

# Search CLI Function
@click.command()
@click.option("--config", type=click.Path(exists=True),
              callback=lambda ctx, param, value: _load_config(ctx, value),
              is_eager=True,
              help="Path to a JSON config file with parameters")
@click.option("--short-name", type=str,
              help="Dataset short name (e.g., 'MOD11A2')", default=None)
@click.option("--concept-id", type=str,
              help="Concept ID for the dataset (takes precedence over short name)", default=None)
@click.option("--temporal", type=TemporalType(),
              help="Temporal range as 'start/end' (e.g., '2020-01-01/2020-01-02')", default=None)
@click.option("--bbox", type=BBoxType(),
              help="Bounding box as 'minLon,minLat,maxLon,maxLat'", default=None)
@click.option("--point", type=PointType(),
              help="A point as 'lon,lat'", default=None)
@click.option("--geojson", type=GeoJSONType(),
              help="Path to a GeoJSON file. Returns exterior points in counterclockwise order", default=None)
@click.option("--count", type=int, help="Number of results to retrieve", default=2000)
@click.option("--output", type=str, help="Output filename (should end in .json or .txt). JSON is nested by granule. Text is un-nested.", default="results.json")
def search(config, short_name, concept_id, temporal, bbox, point, geojson, count, output):
    """
    Searches with the provided parameters and produces outputs using earthaccess.
    
    You can provide arguments on the command line or via a JSON config file (using --config).
    The output format is determined by the file extension on --output.
    """
    # Validate that at least one dataset identifier is provided.
    if not short_name and not concept_id:
        click.echo("Error: Please provide either --short-name or --concept-id.", err=True)
        ctx = click.get_current_context()
        ctx.abort()

    # Build a dictionary of parameters that match what earthaccess.search_data expects.
    search_params = {
        "short_name": short_name,
        "concept_id": concept_id,
        "temporal": temporal,
        "bounding_box": bbox,
        "point": point,
        "polygon": geojson,
        "count": count,
    }

    # Remove keys with a None value.
    search_params = {k: v for k, v in search_params.items() if v is not None}   

    # Pass the validated and converted parameters directly into the search function.
    results = earthaccess.search_data(**search_params)

    # For example, get the data links from each result.
    links = [result.data_links() for result in results]

    # Determine the output format based on the file extension.
    ext = os.path.splitext(output)[1].lower()
    try:
        if ext == ".json":
            with open(output, "w") as f:
                json.dump(links, f, indent=2)
            click.echo(f"Results saved to JSON file: {output}")
        elif ext == ".txt":
            # Flatten the nested list of links.
            flattened_links = []
            for item in links:
                if isinstance(item, (list, tuple)):
                    flattened_links.extend(item)
                else:
                    flattened_links.append(item)
            with open(output, "w") as f:
                for link in flattened_links:
                    f.write(str(link) + "\n")
            click.echo(f"Results saved to text file: {output}")
        else:
            click.echo("Error: Output file extension must be either .json or .txt", err=True)
            ctx = click.get_current_context()
            ctx.abort()
    except Exception as e:
        click.echo(f"Error writing output file: {e}", err=True)
        ctx = click.get_current_context()
        ctx.abort()

def _load_config(ctx, config_path):
    if not config_path:
        return
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        # Update the context's default_map so that command-line options override these
        ctx.default_map = config
    except Exception as e:
        raise click.BadParameter(f"Could not load config file: {e}")

@click.group()
def cli():
    pass

cli.add_command(search)

if __name__ == "__main__":
    cli()
