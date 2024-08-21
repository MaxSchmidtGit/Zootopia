def count_domains(log_file, min_hits=0):
    domain_counts = {}
    lines = log_file.strip().split("\n")
    for line in lines:
        domain, count = line.strip().split()
        count = int(count)
        domain_parts = domain.split(".")
        # Nimm die letzten zwei Teile der Domain für Second-Level-Domains,
        # ansonsten die letzten drei Teile für Third-Level-Domains.
        if len(domain_parts) > 2:
            domain = ".".join(domain_parts[-3:])
        else:
            domain = ".".join(domain_parts[-2:])
        domain_counts[domain] = domain_counts.get(domain, 0) + count

    # Filtere nur die Domains mit Hits >= min_hits
    domain_counts = {domain: count for domain, count in domain_counts.items() if count >= min_hits}

    # Sortiere die Domains: Erst nach Hits absteigend, dann alphabetisch
    sorted_domains = sorted(domain_counts.items(), key=lambda x: (-x[1], x[0]))

    output = "\n".join([f"{domain} ({count})" for domain, count in sorted_domains])

    return output


def main():
    log_file = """
    *.amazon.co.uk    89
    *.doubleclick.net    139
    *.fbcdn.net    212
    *.in-addr.arpa    384
    *.l.google.com    317
    1.client-channel.google.com    110
    6.client-channel.google.com    45
    a.root-servers.net    1059
    apis.google.com    43
    clients4.google.com    71
    clients6.google.com    81
    connect.facebook.net    68
    edge-mqtt.facebook.com    56
    graph.facebook.com    150
    mail.google.com    128
    mqtt-mini.facebook.com    47
    ssl.google-analytics.com    398
    star-mini.c10r.facebook.com    46
    staticxx.facebook.com    48
    www.facebook.com    178
    www.google.com    162
    www.google-analytics.com    127
    www.googleapis.com    87
    """
    print(count_domains(log_file, 500))


if __name__ == "__main__":
    main()
