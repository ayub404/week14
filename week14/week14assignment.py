manifest = [
    {'tag_id': "BAG-001", 'passenger_name': "Wei Chen"},
    {'tag_id': "BAG-002", 'passenger_name': "Anita Roy"},
    {'tag_id': "BAG-003", 'passenger_name': "Leo Das"}
]

scanned = ["BAG-001", "BAG-003", "BAG-999"]

def build_baggage_map(flight_manifest):
    return { item['tag_id']: item['passenger_name'] for item in flight_manifest}

def reconcile_bags(bag_map, scanned_tags):
    scanned_set = set(scanned_tags)
    bag_map_set = set(bag_map)

    mystery_bag =  scanned_set - bag_map_set
    lost_bag = bag_map_set - scanned_set
    return mystery_bag, lost_bag


def generate_lost_report(bag_map, lost_tag_set):
    
    print(f"Lost Bags: {lost_tag_set}")
    print(f"Mystery Bags: {mystery_bag}")
    report = [ f"Missing: Bag {tag} (Owner: {bag_map[tag]})"
        for tag in lost_tag_set
    ]
    print(f"Report: {report}")
dictionary = build_baggage_map(manifest)
mystery_bag, lost_bag = reconcile_bags(dictionary, scanned)
result = generate_lost_report(dictionary, lost_bag)
