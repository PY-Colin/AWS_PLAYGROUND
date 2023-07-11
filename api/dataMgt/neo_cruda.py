from neo4j import GraphDatabase, RoutingControl


URI = "neo4j://localhost:7687"
AUTH = ("spanarchian", "Spanarchian12345!")


def create_entity(qry, data, db="equipment"):
    print("create_entity triggered\n")
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.execute_query(
            qry,
            data=data,
            database_=db,
        )
    print("create_entity completed\n\n")


def update_entity(qry, data, db):
    print("update_entity triggered\n")
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.execute_query(
            qry,
            email=data["email"],
            data=data,
            database_=db,
        )
    print("update_entity completed\n\n")


def read_all_entities(qry, db="equipment"):
    print("read_all_entities triggered\n")
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        records, _, _ = driver.execute_query(
            qry,
            database_=db,
            routing_=RoutingControl.READ,
        )
        print("read_all_entities completed\n\n")
        return records[0]["equip"]


def read_entity_by_email(qry, target, db="equipment"):
    print("read_entity_by_email triggered\n")
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        records, _, _ = driver.execute_query(
            qry,
            email=target,
            database_=db,
            routing_=RoutingControl.READ,
        )
        print("read_entity_by_email completed\n\n")
        return records[0]["equip"]


create_entity(
    "create (a:EQUIPMENT) " "set a +=  $data ",
    {"name": "Emil", "age": 45, "skill": ["Neo4J", "AI"], "email": "emil@neo4j.net"},
    "equipment",
)

create_entity(
    "create (a:EQUIPMENT) " "set a +=  $data ",
    {
        "name": "Jim",
        "age": 45,
        "skill": ["Whovian", "Bike Maniac"],
        "email": "jim@neo4j.net",
    },
    "equipment",
)

resp = read_all_entities(
    "MATCH (a:EQUIPMENT)  RETURN COLLECT(properties(a)) AS  equip ",
    "equipment",
)
print(f"read_all_entities = {resp}")


resp = read_entity_by_email(
    "MATCH (a:EQUIPMENT) where a.email = $email RETURN COLLECT(properties(a)) AS  equip ",
    "jim@neo4j.net",
    "equipment",
)
print(f"entity_by_email = {resp}")


qry = "MATCH (a:EQUIPMENT)  WHERE a.email= $email   set a +=  $data "
data = {
    "name": "Jim Weber",
    "age": 45,
    "skill": ["Whovian", "Bike Maniac"],
    "email": "jim@neo4j.net",
}
db = "equipment"
update_entity(qry, data, db)


resp = read_all_entities(
    "MATCH (a:EQUIPMENT)  RETURN COLLECT(properties(a)) AS  equip ",
    "equipment",
)
print(f"resp = {resp}")
