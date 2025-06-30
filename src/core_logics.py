from sage.api_calls import get_receipt_lines
from datetime import datetime

def get_sage_receipt_lines():
    return get_receipt_lines()

def convert_receipt_lines(receipts):
    '''
    Convert receipts into usable lines to be sent to Zeendoc
    '''
    # We have to comply to the following format (taken from the 
    # 2024-10-03 Mapping SAGE L1000 GESCOM.xlsx file)

    # id_ligne
    # bon_commande
    # nom_br
    # date_commande
    # date_br
    # fournisseur
    # pu_original
    # quantite_originale
    # taux_tva_original
    # total_ligne_original
    # remise_originale
    # ref_article_fournisseur
    # ref_article_erp
    # description_article

    #Format and values accepted by the zeendoc WS
    # {"data":{
    #         "id_ligne": 1,
    #         "bon_commande": "BC",
    #         "nom_br": "BR",
    #         "date_br": "2025-05-13",
    #         "fournisseur": "SUPPLIER",
    #         "pu_original": 2000,
    #         "quantite_originale": 10.0,
    #         "ref_article_fournisseur":"REFARTICLE",
    #         "ref_article_erp": "REF",
    #         "description_article": "des"
    #          }}

# id_ligne	varchar(100)
# type_ligne	varchar(20) NULL
# id_fournisseur	varchar(100) NULL
# num_commande	varchar(100) NULL
# num_ligne	varchar(100) NULL
# num_br	varchar(100) NULL
# num_ligne_br	int(11) NULL
# date_br	varchar(100) NULL
# num_bl	varchar(100) NULL
# code_article_interne	varchar(100) NULL
# code_article_fournisseur	varchar(100) NULL
# designation_article	varchar(255) NULL
# quantite_originale	decimal(14,5) NULL
# pu_original	decimal(14,5) NULL
# total_ligne_original	decimal(14,5) NULL
# total_ligne_retenu	decimal(14,5) NULL
# compte_comptable	varchar(100) NULL
# analytique_1	varchar(100) NULL
# analytique_2	varchar(100) NULL
# analytique_3	varchar(100) NULL
# analytique_4	varchar(100) NULL
# analytique_5	varchar(100) NULL
# document_affected	varchar(100) NULL
# ajout_utilisateur	int(11) NULL
# coll_id_document	varchar(100) NULL
# res_id_document	int(11) NULL
# affected_to_page	int(11) NULL
# affected_to_line	varchar(100) NULL
# coll_id_document2	varchar(100) NULL
# res_id_document2	int(11) NULL
# affected_to_page2	int(11) NULL
# affected_to_line2	varchar(100) NULL
# quantite_corrigee	decimal(14,5) NULL
# pu_corrige	decimal(14,5) NULL
# date_comparaison_auto	timestamp NULL
# date_rapprochement_1	timestamp NULL
# date_rapprochement_2	timestamp NULL
# decision1	varchar(100) NULL
# date_rapprochement_3	timestamp NULL
# decision2	varchar(100) NULL
# date_export_erp	timestamp NULL
# date_export_compta	timestamp NULL
# num_fac_four	varchar(100) NULL
# date_fac_four	varchar(100) NULL
# global_total_ht	decimal(14,5) NULL
# global_total_tva	decimal(14,5) NULL
# global_total_ttc	decimal(14,5) NULL
# devise	varchar(3) NULL
# taux_conversion	decimal(10,7) NULL
# date_import	timestamp NULL
# taux_tva_original	decimal(5,2) NULL
# taux_tva_corrige	decimal(5,2) NULL
# remise_originale	decimal(14,5) NULL
# remise_corrigee	decimal(14,5) NULL
# date_commande	varchar(100) NULL
# new_line_tax	tinyint(4) NULL
# new_line_article	tinyint(4) NULL
# pu_fact_inf_commande	tinyint(4) NULL
# pu_fact_sup_commande	tinyint(4) NULL
# qte_fact_inf_commande	tinyint(4) NULL
# qte_fact_sup_commande	tinyint(4) NULL
# remise_fact_inf_commande	tinyint(4) NULL
# remise_fact_sup_commande	tinyint(4) NULL
# total_ligne_inf_commande	tinyint(4) NULL
# total_ligne_sup_commande	tinyint(4) NULL
# decision_avoir_demande	tinyint(4) NULL
# decision_commande_regul	tinyint(4) NULL
# decision_base_tarif_regul	tinyint(4) NULL
# decision_att_fact_compl	tinyint(4) NULL
# taux_tva_fact_inf_commande	tinyint(4) NULL
# taux_tva_fact_sup_commande	tinyint(4) NULL


    #RAW SAGE LINE : 
    return [
            {
                "id_ligne": item["id_ligne"],
                "num_br": item["id_ligne"],
                "date_br": datetime.fromisoformat(item["date_br"]).strftime("%Y-%m-%d"),
                "id_fournisseur": item["fournisseur"],
                "num_ligne": item["id_ligne"],
                "pu_original": item["pu_original"],
                "quantite_originale": item["quantite_original"],
                "total_ligne_retenu": item["total_ligne_retenu"],
                "code_article_interne": item["ref_article_erp"],
                "code_article_fournisseur": item["ref_article_fournisseur_retenue"],
                "remise_originale": item["remise_retenue"],
                "num_commande": item["bon_commande"],
                "designation_article": item["description_article"]
            } for data in receipts["Receptions"] for item in data["lines"] if data is not None            # a line has been of NoneType so we add this condition
            ]

    # mapped_line = {
    #         "id_ligne": item["id_ligne"],
    #
    #         }

    # previous mapping
    return [
            {
            "id_ligne": item["id_ligne"],
            "bon_commande": item["bon_commande"],
            "nom_br": item["nom_br"],
            # "date_commande" is missing from the response
            "date_br": datetime.fromisoformat(item["date_br"]
                                              ).strftime("%Y-%m-%d"),
            "fournisseur": item["fournisseur"],
            "pu_original": item["pu_original"],
            "quantite_originale": item["quantite_original"],
            # renamed the key here for orthograph purpose
            # "taux_tva_original" is missing
            # "total_ligne original" is missing
            # "remise_originale" is missing
            "ref_article_fournisseur":
                item["ref_article_fournisseur_retenue"],
            # "ref_article_fournisseur_retenue" : correct key name / value ? 
            "ref_article_erp": item["ref_article_erp"],
            "description_article": item["description_article"],
             } for data in receipts["Receptions"] for item in data["lines"] if data is not None            # a line has been of NoneType so we add this condition
            ]
