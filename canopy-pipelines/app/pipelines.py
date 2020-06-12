from dagster import pipeline
from solids import (
    load_items_reference_db,
    load_secop_join,
    process_alarm_sobrecosto,
    save_alarm_sobrecosto
)


@pipeline
def sobrecostos_pipeline():
    precios_reference = load_items_reference_db()
    secop_join = load_secop_join()

    save_alarm_sobrecosto(process_alarm_sobrecosto(secop_join, precios_reference))
