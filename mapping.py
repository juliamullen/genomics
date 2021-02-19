def get_customized_mapping(cls):
    return {
            "mutations": {
                "type": "nested",
                "properties": {
                    "type": {
                        "type": "keyword"
                        },
                    "mutation": {
                        "type": "keyword"
                        },
                    "gene": {
                        "type": "keyword"
                        },
                    "ref_codon": {
                        "type": "keyword"
                        },
                    "pos": {
                        "type": "keyword"
                        },
                    "alt_codon": {
                        "type": "keyword"
                        },
                    "is_synonymous": {
                        "type": "keyword"
                        },
                    "ref_aa": {
                        "type": "keyword"
                        },
                    "codon_num": {
                        "type": "keyword"
                        },
                    "alt_aa": {
                        "type": "keyword"
                        },
                    "absolute_coords": {
                        "type": "keyword"
                        },
                    "change_length_nt": {
                        "type": "keyword"
                        },
                    "nt_map_coords": {
                        "type": "keyword"
                        },
                    "aa_map_coords": {
                        "type": "keyword"
                        }
                    }
                },
            "division": {
                "type": "keyword",
                "normalizer": "keyword_lowercase_normalizer"

                },
        "country": {
                "type": "keyword",
                "normalizer": "keyword_lowercase_normalizer"

                },
        "date_submitted": {
                "type": "keyword"
                },
        "date_collected": {
                "type": "keyword"
                },
        "date_modified": {
                "type": "keyword"
                },
        "country_id": {
                "type": "keyword"
                },
        "authors": {
                "type": "keyword"
                },
        "pangolin_lineage": {
                "type": "keyword",
                "normalizer": "keyword_lowercase_normalizer"

                },
        "location": {
                "type": "keyword"
                },
        "division_id": {
                "type": "keyword"
                },
        "accession_id": {
                "type": "keyword"
                },
        "clade": {
                "type": "keyword"
                },
        "pango_version": {
                "type": "keyword"
                },
        "country_normed": {
                "type": "keyword"
                }

}
