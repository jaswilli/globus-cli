from __future__ import print_function

import json


def display_name_or_cname(ep_doc):
    return ep_doc['display_name'] or ep_doc['canonical_name']


def print_json_from_iterator(iterator):
    json_output_dict = {'DATA': []}
    for item in iterator:
        json_output_dict['DATA'].append(item.data)
    print(json.dumps(json_output_dict))


def text_header_and_format(lengths_and_headers):
    format_lengths = [max(l, len(h)) for (l, h) in lengths_and_headers]
    format_str = ' | '.join('{:' + str(l) + '}' for l in format_lengths)

    print(format_str.format(*[h for (l, h) in lengths_and_headers]))
    print(format_str.format(*['-'*l for l in format_lengths]))

    return format_str


def endpoint_list_to_text(iterator):
    text_col_format = text_header_and_format(
        [(32, 'Owner'), (36, 'ID'), (None, 'Display Name')])

    for result in iterator:
        print(text_col_format.format(
            result.data['owner_string'], result.data['id'],
            display_name_or_cname(result.data)))