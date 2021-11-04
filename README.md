# Aave Set Fallback Oracle Function Agent

## Description

This agent detects Aave Price Oracle `setFallbackOracle` function is called.

## Supported Chains

- Ethereum

## Alerts

Describe each of the type of alerts fired by this agent

- AAVE-1
  - Fired when a transaction contains `setFallbackOracle` function call.
  - Severity is always set to "critical"
  - Type is always set to "suspicious" 
  - The agent returns `fallback_oracle` which is function input for "setFallbackOracle" function and `tx_hash` which is transaction hash metadata.

## Test Data

The agent behaviour can be verified with the following transactions:

- 0x9d2c419069be3ef6b78d6bdb47f6c195e4cb24b25e5706a497731ede033e0503 