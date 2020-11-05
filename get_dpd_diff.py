import requests

if __name__ == '__main__':

    resp = requests.get(
        'https://gitlab.euclid-sgs.uk/api/v4/projects/1480/repository/compare?from=temp-8.0.4&to=8.0.3&straight=true',
        headers={
            'Content-Type': 'application/json',
            'PRIVATE-TOKEN': 'Cdxv9yaCiBqavr9gv9Gr'
        }
    )

    response = resp.json()

    impacted = []
    for diff in response['diffs']:
        if not diff['new_file'] and diff['old_path'] not in impacted:
            impacted.append(diff['old_path'].replace('dataproducts/', '').replace('.xml', ''))

    with open('output.txt', 'w') as f:
        for dpd in impacted:
            if dpd.startswith('Dpd'):
                f.write(dpd+'\n')
