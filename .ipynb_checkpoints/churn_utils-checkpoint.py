def get_churn_prevention_suggestions(customer):
    suggestions = []
    if customer.get('Contract_One year') == 0 and customer.get('Contract_Two year') == 0:
        suggestions.append("Offer long-term contract discounts.")

    if customer.get('TechSupport_Yes') == 0:
        suggestions.append("Provide free technical support for 6 months.")

    if customer.get('InternetService_Fiber optic') == 1:
        suggestions.append("Offer bundle packages for fiber users.")

    if customer.get('tenure') < 6:
        suggestions.append("Launch a loyalty program for new users.")

    return suggestions if suggestions else ["No urgent actions needed."]
