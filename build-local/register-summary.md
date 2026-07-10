# DSSC Dataspace ODRL Policy Building Blocks

Building blocks for ODRL-based access and usage policies as exchanged through the Dataspace Protocol and used by dataspace connectors such as Eclipse EDC and TNO TSG.


## Building Blocks

### `nl.geonovum.dssc.odrl.action-access` — Dataspace Access Action

**Type:** schema

The access action pattern for access policies and offer visibility.

### `nl.geonovum.dssc.odrl.action-use` — ODRL Use Action

**Type:** schema

The ODRL use action for usage policies.

### `nl.geonovum.dssc.odrl.constraint-atomic` — ODRL Atomic Constraint

**Type:** schema

A basic ODRL constraint with left operand, operator and right operand.

### `nl.geonovum.dssc.odrl.location-privacy.geofence-credential-reference` — Participant Geofence Credential Reference

**Type:** schema

A Verifiable Credential subject shape that references a participant geofence by resolvable URL and SHA-256 hash.

### `nl.geonovum.dssc.odrl.location-privacy.action-aggregate` — Location Privacy Aggregate Action

**Type:** schema

Action indicating that transferred spatial data must be aggregated to a larger spatial unit.

### `nl.geonovum.dssc.odrl.location-privacy.action-pseudonymize-location` — Location Privacy Pseudonymize Location Action

**Type:** schema

Action indicating that the spatial reference must be pseudonymized before transfer.

### `nl.geonovum.dssc.odrl.location-privacy.action-reduce-accuracy` — Location Privacy Reduce Positional Accuracy Action

**Type:** schema

Action indicating that the spatial reference must be generalized or degraded to a lower positional accuracy or resolution.

### `nl.geonovum.dssc.odrl.location-privacy.action-remove-location` — Location Privacy Remove Location Action

**Type:** schema

Action indicating that the spatial reference must be removed from transferred data.

### `nl.geonovum.dssc.odrl.location-privacy.action-remove-sensitive-attributes` — Location Privacy Remove Sensitive Attributes Action

**Type:** schema

Action indicating that sensitive non-spatial attributes must be removed or degraded while keeping the original spatial reference.

### `nl.geonovum.dssc.odrl.location-privacy.action-within-geofence` — Location Privacy Within Geofence Action

**Type:** schema

Action indicating that transferred spatial data must be filtered or clipped to the consumer participant geofence.

### `nl.geonovum.dssc.odrl.constraint-logical` — ODRL Logical Constraint

**Type:** schema

A logical composition of ODRL constraints using and, or or xone.

### `nl.geonovum.dssc.odrl.location-privacy.constraint-aggregation-parameters` — Aggregation Parameter Constraints

**Type:** schema

ODRL constraints defining the location aggregation algorithm and minimum grid resolution or anonymity parameter.

### `nl.geonovum.dssc.odrl.location-privacy.constraint-geofence-filter` — Geofence Filter Constraint

**Type:** schema

ODRL constraint describing the filter expression used to select or verify features against the consumer geofence.

### `nl.geonovum.dssc.odrl.location-privacy.constraint-geofence-vc-present` — Geofence Credential Presence Constraints

**Type:** schema

ODRL constraints requiring both geofence URL and geofence hash values to be present in a participant credential.

### `nl.geonovum.dssc.odrl.location-privacy.constraint-positional-accuracy` — Positional Accuracy Constraint

**Type:** schema

ODRL constraint defining a target minimum positional accuracy or resolution for generalized location data.

### `nl.geonovum.dssc.odrl.obligation` — ODRL Obligation / Duty Rule

**Type:** schema

An obligation or duty rule expressing an action that must be fulfilled.

### `nl.geonovum.dssc.odrl.permission` — ODRL Permission Rule

**Type:** schema

A permission rule allowing an action under optional constraints and/or duties.

### `nl.geonovum.dssc.odrl.prohibition` — ODRL Prohibition Rule

**Type:** schema

A prohibition rule disallowing an action under optional constraints.

### `nl.geonovum.dssc.odrl.agreement` — ODRL Agreement for Dataspace Protocol

**Type:** schema

An ODRL Agreement profile for negotiated dataspace contracts.

### `nl.geonovum.dssc.odrl.offer` — ODRL Offer for Dataspace Protocol

**Type:** schema

An ODRL Offer profile for contract offers in catalog and negotiation flows.

### `nl.geonovum.dssc.odrl.policy-set` — ODRL Policy Set for Dataspace Protocol

**Type:** schema

A constrained ODRL Set profile for policies exchanged through the Dataspace Protocol.

### `nl.geonovum.dssc.odrl.location-privacy.patterns.ldp1-geofence-vc-required` — LDP1 Geofence Credential Required

**Type:** schema

Contract-negotiation policy requiring a participant geofence credential with URL and hash.

### `nl.geonovum.dssc.odrl.location-privacy.patterns.ldp1-within-geofence` — LDP1 Within Geofence Transfer Duty

**Type:** schema

Data-transfer policy requiring a Location Privacy Proxy to filter or clip results to the participant geofence.

### `nl.geonovum.dssc.odrl.location-privacy.patterns.ldp2-degrade-sensitive-attributes` — LDP2 Remove or Degrade Sensitive Attributes

**Type:** schema

Data-transfer policy retaining original spatial reference while removing or degrading selected sensitive attributes.

### `nl.geonovum.dssc.odrl.location-privacy.patterns.ldp3-remove-location` — LDP3 Remove Spatial Reference

**Type:** schema

Data-transfer policy requiring removal of geometry or spatial reference before sharing attributes.

### `nl.geonovum.dssc.odrl.location-privacy.patterns.ldp4-pseudonymize-location` — LDP4 Pseudonymize Spatial Reference

**Type:** schema

Data-transfer policy requiring pseudonymization of location so that direct coordinates are replaced by pseudonymous spatial identifiers.

### `nl.geonovum.dssc.odrl.location-privacy.patterns.ldp5-reduce-positional-accuracy` — LDP5 Reduce Positional Accuracy

**Type:** schema

Data-transfer policy requiring location data to be generalized to a defined minimum positional accuracy or resolution.

### `nl.geonovum.dssc.odrl.location-privacy.patterns.ldp6-aggregate-hexgrid` — LDP6 Aggregate to Hexagonal Grid

**Type:** schema

Data-transfer policy requiring spatial aggregation to a hexagonal grid with a defined minimum resolution.

### `nl.geonovum.dssc.odrl.patterns.access-by-participant-credential` — Access by Participant Credential

**Type:** schema

Allows use only when the requesting participant has a required verifiable credential or claim.

### `nl.geonovum.dssc.odrl.patterns.no-redistribution` — No Redistribution

**Type:** schema

Allows use while explicitly prohibiting redistribution.

### `nl.geonovum.dssc.odrl.patterns.purpose-limitation` — Purpose Limitation

**Type:** schema

Allows use only for a declared purpose.

### `nl.geonovum.dssc.odrl.patterns.time-limited-use` — Time-Limited Use

**Type:** schema

Allows use for a limited duration after contract agreement.

