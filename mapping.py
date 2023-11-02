def mapping_data_mutless(cls):
    return {
        "mutations": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "division": {
            "type": "keyword",
        },
        "division_lower": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "country": {
            "type": "keyword",
        },
        "country_lower": {
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
        "pangolin_lineage": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "pangolin_lineage_crumbs": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "location": {
            "type": "keyword"
        },
        "location_lower": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "location_id": {
            "type": "keyword"
        },
        "division_id": {
            "type": "keyword"
        },
        "accession_id": {
            "type": "keyword"
        }
    }


def mapping_data_muts(cls):
    return {
        "type": {
            "type": "keyword"
        },
        "mutation": {
            "type": "keyword",
            "normalizer": "keyword_lowercase_normalizer"
        },
        "gene": {
            "type": "keyword"
        },
        "ref_codon": {
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
        }
    }
