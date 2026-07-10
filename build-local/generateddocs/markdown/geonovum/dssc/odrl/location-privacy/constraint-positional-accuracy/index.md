
# Positional Accuracy Constraint (Schema)

`nl.geonovum.dssc.odrl.location-privacy.constraint-positional-accuracy` *v0.1.0*

ODRL constraint defining a target minimum positional accuracy or resolution for generalized location data.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Positional Accuracy Constraint
#### json
```json
{
  "leftOperand": "lp:positionalAccuracyMeters",
  "operator": "gte",
  "rightOperand": 100
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/location-privacy/constraint-positional-accuracy/schema.json
title: Positional Accuracy Constraint
type: object
required:
- leftOperand
- operator
- rightOperand
properties:
  leftOperand:
    const: lp:positionalAccuracyMeters
  operator:
    enum:
    - gte
    - gteq
  rightOperand:
    type: number
    exclusiveMinimum: 0
additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/constraint-positional-accuracy/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/constraint-positional-accuracy/schema.yaml)

## Sources

* [Using Sensitive Location Data to its Full Potential - wetransform](https://wetransform.to/news-and-events/sensitive-location-data-full-potential/)
* [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [ODRL V2.2 Implementation Best Practices](https://w3c.github.io/odrl/bp/)
* [SAGE WP2 Meeting - Location Data Policies in the EDC](urn:local:SAGE-WP2-Meeting-Location-Data-Policies-in-the-EDC.pdf)
