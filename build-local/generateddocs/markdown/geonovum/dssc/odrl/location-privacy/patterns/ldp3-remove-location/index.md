
# LDP3 Remove Spatial Reference (Schema)

`nl.geonovum.dssc.odrl.location-privacy.patterns.ldp3-remove-location` *v0.1.0*

Data-transfer policy requiring removal of geometry or spatial reference before sharing attributes.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Generic ODRL location policy example
#### json
```json
{
  "@context": [
    "https://www.w3.org/ns/odrl.jsonld",
    {
      "lp": "https://wetransform.eu/ns/odrl/location-privacy#",
      "geofence": "https://wetransform.eu/ns/vc/geofence#",
      "vc": "https://www.w3.org/2018/credentials#"
    }
  ],
  "@type": "odrl:Set",
  "uid": "urn:policy:ldp-remove-location",
  "permission": [
    {
      "target": "urn:asset:protected-resource",
      "action": "use",
      "duty": [
        {
          "action": "lp:removeLocation",
          "constraint": [
            {
              "leftOperand": "lp:geometrySelector",
              "operator": "eq",
              "rightOperand": "$.features[*].geometry"
            }
          ]
        }
      ]
    }
  ]
}

```


### Eclipse EDC example
#### json
```json
{
  "@context": [
    "https://www.w3.org/ns/odrl.jsonld",
    {
      "lp": "https://wetransform.eu/ns/odrl/location-privacy#",
      "geofence": "https://wetransform.eu/ns/vc/geofence#",
      "vc": "https://www.w3.org/2018/credentials#"
    }
  ],
  "@type": "odrl:Set",
  "uid": "urn:policy:ldp-remove-location",
  "permission": [
    {
      "target": "urn:asset:protected-resource",
      "action": "use",
      "duty": [
        {
          "action": "lp:removeLocation",
          "constraint": [
            {
              "leftOperand": "lp:geometrySelector",
              "operator": "eq",
              "rightOperand": "$.features[*].geometry"
            }
          ]
        }
      ]
    }
  ]
}

```


### Location Privacy Proxy example
#### json
```json
{
  "@context": [
    "https://www.w3.org/ns/odrl.jsonld",
    {
      "lp": "https://wetransform.eu/ns/odrl/location-privacy#",
      "geofence": "https://wetransform.eu/ns/vc/geofence#",
      "vc": "https://www.w3.org/2018/credentials#"
    }
  ],
  "@type": "odrl:Set",
  "uid": "urn:policy:ldp-remove-location",
  "permission": [
    {
      "target": "urn:asset:protected-resource",
      "action": "use",
      "duty": [
        {
          "action": "lp:removeLocation",
          "constraint": [
            {
              "leftOperand": "lp:geometrySelector",
              "operator": "eq",
              "rightOperand": "$.features[*].geometry"
            }
          ]
        }
      ]
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/location-privacy/patterns/ldp3-remove-location/schema.json
title: LDP3 Remove Spatial Reference
$ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/policy-set/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/patterns/ldp3-remove-location/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/patterns/ldp3-remove-location/schema.yaml)

## Sources

* [Using Sensitive Location Data to its Full Potential - wetransform](https://wetransform.to/news-and-events/sensitive-location-data-full-potential/)
* [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [ODRL V2.2 Implementation Best Practices](https://w3c.github.io/odrl/bp/)
* [SAGE WP2 Meeting - Location Data Policies in the EDC](urn:local:SAGE-WP2-Meeting-Location-Data-Policies-in-the-EDC.pdf)
