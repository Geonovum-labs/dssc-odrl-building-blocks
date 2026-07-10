
# Geofence Filter Constraint (Schema)

`nl.geonovum.dssc.odrl.location-privacy.constraint-geofence-filter` *v0.1.0*

ODRL constraint describing the filter expression used to select or verify features against the consumer geofence.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Geofence Filter Constraint
#### json
```json
{
  "leftOperand": "lp:geofenceFilter",
  "operator": "isPartOf",
  "rightOperand": "$.features[?(@.geometry.passesConsumerGeofence())]"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/location-privacy/constraint-geofence-filter/schema.json
title: Geofence Filter Constraint
type: object
required:
- leftOperand
- operator
- rightOperand
properties:
  leftOperand:
    const: lp:geofenceFilter
  operator:
    enum:
    - isPartOf
    - odrl:isPartOf
  rightOperand:
    type: string
additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/constraint-geofence-filter/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/constraint-geofence-filter/schema.yaml)

## Sources

* [Using Sensitive Location Data to its Full Potential - wetransform](https://wetransform.to/news-and-events/sensitive-location-data-full-potential/)
* [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [ODRL V2.2 Implementation Best Practices](https://w3c.github.io/odrl/bp/)
* [SAGE WP2 Meeting - Location Data Policies in the EDC](urn:local:SAGE-WP2-Meeting-Location-Data-Policies-in-the-EDC.pdf)
