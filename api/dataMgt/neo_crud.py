from neo4j import GraphDatabase, RoutingControl


URI = "neo4j://localhost:7687"
AUTH = ("spanarchian", "Spanarchian12345!")


def create_entity(driver, qry, data, db="equipment"):
    driver.execute_query(
        qry,
        data=data,
        database_=db,
    )


def update_entity():
    pass


def read_all_entities(driver, qry, db="equipment"):
    records, _, _ = driver.execute_query(
        qry,
        database_=db,
        routing_=RoutingControl.READ,
    )
    return records[0]["equip"]


def read_entity_by_id():
    pass


with GraphDatabase.driver(URI, auth=AUTH) as driver:
    create_entity(
        driver,
        "create (a:EQUIPMENT) " "set a +=  $data ",
        {"name": "Emil", "age": 45, "skill": ["Neo4J", "AI"]},
        "equipment",
    )

    create_entity(
        driver,
        "create (a:EQUIPMENT) " "set a +=  $data ",
        {"name": "Jim", "age": 45, "skill": ["Whovian", "Bike Maniac"]},
        "equipment",
    )

    resp = read_all_entities(
        driver,
        "MATCH (a:EQUIPMENT)  RETURN COLLECT(properties(a)) AS  equip ",
        "equipment",
    )

    print(f"resp = {resp}")
