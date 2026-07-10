
# Purpose Limitation (Schema)

`nl.geonovum.dssc.odrl.patterns.purpose-limitation` *v0.1.0*

Allows use only for a declared purpose.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Generic ODRL example
#### json
```json
{
  "@context": [
    "https://www.w3.org/ns/odrl.jsonld",
    {
      "ex": "https://example.org/policy/"
    }
  ],
  "@type": "Set",
  "permission": [
    {
      "action": "use",
      "constraint": {
        "leftOperand": "ex:purpose",
        "operator": "eq",
        "rightOperand": "ex:UrbanPlanning"
      }
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
      "ex": "https://example.org/policy/"
    }
  ],
  "@type": "Set",
  "permission": [
    {
      "action": "use",
      "constraint": {
        "leftOperand": "ex:purpose",
        "operator": "eq",
        "rightOperand": "ex:UrbanPlanning"
      }
    }
  ]
}

```


### TNO TSG example
#### json
```json
{
  "@context": [
    "https://www.w3.org/ns/odrl.jsonld",
    {
      "ex": "https://example.org/policy/"
    }
  ],
  "@type": "Set",
  "permission": [
    {
      "action": "use",
      "constraint": {
        "leftOperand": "ex:purpose",
        "operator": "eq",
        "rightOperand": "ex:UrbanPlanning"
      }
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/patterns/purpose-limitation/schema.json
title: Purpose Limitation
$ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/policy-set/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/patterns/purpose-limitation/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/patterns/purpose-limitation/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
