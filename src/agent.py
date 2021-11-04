from forta_agent import Finding, FindingType, FindingSeverity
from .constants import AAVE_PRICE_ORACLE_ADDRESS, SET_FALLBACK_ORACLE_FUNCTION_ABI


def handle_transaction(transaction_event):
    findings = []
    set_fallback_oracle_invocations = transaction_event.filter_function(SET_FALLBACK_ORACLE_FUNCTION_ABI, AAVE_PRICE_ORACLE_ADDRESS)
    print(transaction_event)

    for invocation in set_fallback_oracle_invocations:
        args = invocation[1]
        findings.append(Finding({
            'name': 'Aave Set Fallback Oracle Function Agent',
            'description': f'AavepriceOracle.setFallbackOracle() function is called. Fallback oracle value: {args["fallbackOracle"]}',
            'alert_id': 'AAVE-1',
            'type': FindingType.Suspicious,
            'severity': FindingSeverity.Critical,
            'metadata': {
                'fallback_oracle': args['fallbackOracle'],
                'tx_hash': transaction_event.hash
            }
        }))
    return findings

