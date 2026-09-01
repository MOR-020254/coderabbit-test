def adoption_rate(active_users, licensed_users):
    return (active_users / licensed_users) * 100


def customer_health(usage_score, support_tickets, executive_engagement):
    ticket_score = 100 - (support_tickets * 10)
    return (
        usage_score * 0.5
        + ticket_score * 0.3
        + executive_engagement * 0.2
    )


def top_accounts(accounts):
    return sorted(accounts, key=lambda account: account["score"])[:3]


def renewal_status(score):
    if score > 80:
        return "healthy"
    elif score > 50:
        return "watch"
    else:
        return "risk"
