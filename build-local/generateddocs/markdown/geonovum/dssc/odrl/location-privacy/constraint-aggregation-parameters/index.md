
# Aggregation Parameter Constraints (Schema)

`nl.geonovum.dssc.odrl.location-privacy.constraint-aggregation-parameters` *v0.1.0*

ODRL constraints defining the location aggregation algorithm and minimum grid resolution or anonymity parameter.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Aggregation Parameter Constraints
#### json
```json
[
  {
    "leftOperand": "lp:algo",
    "operator": "eq",
    "rightOperand": "lp:HexGridAgg"
  },
  {
    "leftOperand": "lp:hexGridRes",
    "operator": "gte",
    "rightOperand": 8
  }
]

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/location-privacy/constraint-aggregation-parameters/schema.json
title: Aggregation Parameter Constraints
type: array
minItems: 2
items:
  $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-atomic/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/constraint-aggregation-parameters/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/constraint-aggregation-parameters/schema.yaml)

## Sources

* [Using Sensitive Location Data to its Full Potential - wetransform](https://wetransform.to/news-and-events/sensitive-location-data-full-potential/)
* [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [ODRL V2.2 Implementation Best Practices](https://w3c.github.io/odrl/bp/)
* [SAGE WP2 Meeting - Location Data Policies in the EDC](urn:local:SAGE-WP2-Meeting-Location-Data-Policies-in-the-EDC.pdf)
