import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from .routes import route_events
from .routes import route_people
from .routes import route_equipment
from .routes import route_locations
from .routes import route_organisations

from .reports import report_CIP
from .reports import report_Comparison
from .reports import report_Readiness


###############################################################################
#   Application object                                                        #
###############################################################################
app = FastAPI()


@app.get("/health")
def health():
    return {"api_status": "active", "api_version": "v0.0.1"}


#   Routers configuration
app.include_router(route_events.router, prefix="/event", tags=["INGEST", "EVENT"])
app.include_router(route_people.router, prefix="/people", tags=["INGEST", "PEOPLE"])
app.include_router(
    route_equipment.router, prefix="/equipment", tags=["INGEST", "EQUIPMENT"]
)
app.include_router(
    route_locations.router, prefix="/location", tags=["INGEST", "LOCATION"]
)
app.include_router(
    route_organisations.router, prefix="/orgs", tags=["INGEST", "ORGANISATIONS"]
)


app.include_router(
    report_CIP.router, prefix="/report/ip", tags=["EXTRACT", "INTEL_PIC"]
)
app.include_router(
    report_Readiness.router, prefix="/report/readiness", tags=["EXTRACT", "READINESS"]
)
app.include_router(
    report_Comparison.router,
    prefix="/report/comparison",
    tags=["EXTRACT", "COMPARISON"],
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
