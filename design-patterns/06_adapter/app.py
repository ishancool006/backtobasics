from analytics.factory.adapter_factory import DBFactory

def show_some_results():
    db_object = DBFactory.create()
    db_object.connect()
    results = db_object.execute("max")
    print(results)

if __name__ == "__main__":
    show_some_results()
