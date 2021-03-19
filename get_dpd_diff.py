import requests

if __name__ == '__main__':

    resp = requests.get(
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
