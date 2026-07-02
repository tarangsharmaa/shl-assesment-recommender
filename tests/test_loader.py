from app.core.catalog_loader import CatalogLoader

loader = CatalogLoader("data/shl_product_catalog.json")

catalog = loader.load_catalog()

print("Total Assessments:", len(catalog))
print()

print("First Assessment")
print("----------------")
print(catalog[0])