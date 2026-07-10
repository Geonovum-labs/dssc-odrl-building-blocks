
# Access by Participant Credential (Schema)

`nl.geonovum.dssc.odrl.patterns.access-by-participant-credential` *v0.1.0*

Allows use only when the requesting participant has a required verifiable credential or claim.

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
        "leftOperand": "ex:hasCredentialType",
        "operator": "eq",
        "rightOperand": "ex:TrustedParticipantCredential"
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
        "leftOperand": "ex:hasCredentialType",
        "operator": "eq",
        "rightOperand": "ex:TrustedParticipantCredential"
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
        "leftOperand": "ex:hasCredentialType",
        "operator": "eq",
        "rightOperand": "ex:TrustedParticipantCredential"
      }
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/patterns/access-by-participant-credential/schema.json
title: Access by Participant Credential
$ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/policy-set/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/patterns/access-by-participant-credential/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/patterns/access-by-participant-credential/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
