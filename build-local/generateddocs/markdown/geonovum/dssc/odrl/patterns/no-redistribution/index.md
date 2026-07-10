
# No Redistribution (Schema)

`nl.geonovum.dssc.odrl.patterns.no-redistribution` *v0.1.0*

Allows use while explicitly prohibiting redistribution.

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
      "action": "use"
    }
  ],
  "prohibition": [
    {
      "action": "ex:redistribute"
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
      "action": "use"
    }
  ],
  "prohibition": [
    {
      "action": "ex:redistribute"
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
      "action": "use"
    }
  ],
  "prohibition": [
    {
      "action": "ex:redistribute"
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/patterns/no-redistribution/schema.json
title: No Redistribution
$ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/policy-set/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/patterns/no-redistribution/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/patterns/no-redistribution/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
