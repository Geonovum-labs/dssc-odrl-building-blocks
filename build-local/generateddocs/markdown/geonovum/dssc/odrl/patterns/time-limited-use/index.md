
# Time-Limited Use (Schema)

`nl.geonovum.dssc.odrl.patterns.time-limited-use` *v0.1.0*

Allows use for a limited duration after contract agreement.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Generic ODRL example
#### json
```json
{
  "@context": {
    "edc": "https://w3id.org/edc/v0.0.1/ns/",
    "@vocab": "http://www.w3.org/ns/odrl.jsonld"
  },
  "@type": "Offer",
  "target": "urn:example:dataset:1",
  "permission": [
    {
      "action": "use",
      "constraint": {
        "and": [
          {
            "leftOperand": "edc:inForceDate",
            "operator": "gt",
            "rightOperand": {
              "@value": "contractAgreement",
              "@type": "edc:dateExpression"
            }
          },
          {
            "leftOperand": "edc:inForceDate",
            "operator": "lt",
            "rightOperand": {
              "@value": "contractAgreement + 100d",
              "@type": "edc:dateExpression"
            }
          }
        ]
      }
    }
  ]
}

```


### Eclipse EDC example
#### json
```json
{
  "@context": {
    "edc": "https://w3id.org/edc/v0.0.1/ns/",
    "@vocab": "http://www.w3.org/ns/odrl.jsonld"
  },
  "@type": "Offer",
  "target": "urn:example:dataset:1",
  "permission": [
    {
      "action": "use",
      "constraint": {
        "and": [
          {
            "leftOperand": "edc:inForceDate",
            "operator": "gt",
            "rightOperand": {
              "@value": "contractAgreement",
              "@type": "edc:dateExpression"
            }
          },
          {
            "leftOperand": "edc:inForceDate",
            "operator": "lt",
            "rightOperand": {
              "@value": "contractAgreement + 100d",
              "@type": "edc:dateExpression"
            }
          }
        ]
      }
    }
  ]
}

```


### TNO TSG example
#### json
```json
{
  "@context": {
    "edc": "https://w3id.org/edc/v0.0.1/ns/",
    "@vocab": "http://www.w3.org/ns/odrl.jsonld"
  },
  "@type": "Offer",
  "target": "urn:example:dataset:1",
  "permission": [
    {
      "action": "use",
      "constraint": {
        "and": [
          {
            "leftOperand": "edc:inForceDate",
            "operator": "gt",
            "rightOperand": {
              "@value": "contractAgreement",
              "@type": "edc:dateExpression"
            }
          },
          {
            "leftOperand": "edc:inForceDate",
            "operator": "lt",
            "rightOperand": {
              "@value": "contractAgreement + 100d",
              "@type": "edc:dateExpression"
            }
          }
        ]
      }
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/patterns/time-limited-use/schema.json
title: Time-Limited Use
$ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/offer/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/patterns/time-limited-use/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/patterns/time-limited-use/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
