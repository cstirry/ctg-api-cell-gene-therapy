import pandas as pd


def process_study_data(studies):
    study_data = []

    for study in studies:
        protocol_section = study.protocol_section
        if protocol_section:
            # Get IdentificationModule fields
            identification_module = protocol_section.identification_module
            nct_id = identification_module.nct_id
            brief_title = identification_module.brief_title
            official_title = identification_module.official_title if identification_module else None
            funder_agency_class = (
                identification_module.organization.var_class.name
                if identification_module and identification_module.organization and identification_module.organization.var_class
                else None
            )

            # Get DescriptionModule fields
            description_module = protocol_section.description_module
            brief_summary = description_module.brief_summary if description_module else None
            detailed_description = description_module.detailed_description if description_module else None

            # Get StatusModule fields
            status_module = protocol_section.status_module
            last_update_post_date = status_module.last_update_post_date_struct.var_date if status_module else None
            first_post_date = status_module.study_first_post_date_struct.var_date if status_module else None
            status = status_module.overall_status.name if status_module else None

            # Get DesignModule fields
            design_module = protocol_section.design_module
            study_type = design_module.study_type.name if design_module else None
            phases = [phase.name for phase in design_module.phases] if design_module and design_module.phases else []

            # Get SponsorCollaboratorsModule fields
            sponsor_collaborators_module = protocol_section.sponsor_collaborators_module
            sponsor = sponsor_collaborators_module.lead_sponsor.name if sponsor_collaborators_module and sponsor_collaborators_module.lead_sponsor else None
            collaborators = [collaborator.name for collaborator in
                             sponsor_collaborators_module.collaborators] if sponsor_collaborators_module and sponsor_collaborators_module.collaborators else None

            # Get ConditionsModule fields
            conditions_module = protocol_section.conditions_module
            conditions = conditions_module.conditions if conditions_module else None
            keywords = conditions_module.keywords if conditions_module and conditions_module.keywords else None

            # Get ArmsInterventionsModule fields
            arms_interventions_module = protocol_section.arms_interventions_module
            interventions = [intervention.name for intervention in
                             arms_interventions_module.interventions] if arms_interventions_module and arms_interventions_module.interventions else None

            # Get ContactsLocationsModule fields
            contacts_locations_module = protocol_section.contacts_locations_module
            location_facility = [location.facility for location in
                                 contacts_locations_module.locations] if contacts_locations_module and contacts_locations_module.locations else None
            country = [location.country for location in
                       contacts_locations_module.locations] if contacts_locations_module and contacts_locations_module.locations else None
            geo_point = [location.geo_point for location in
                         contacts_locations_module.locations] if contacts_locations_module and contacts_locations_module.locations else None

            # Append the data to the list
            study_data.append({
                "nct_id": nct_id,
                "brief_title": brief_title,
                "official_title": official_title,
                "brief_summary": brief_summary,
                "detailed_description": detailed_description,
                "conditions": conditions,
                "interventions": interventions,
                "status": status,
                "study_type": study_type,
                "phases": phases,
                "funder_agency_class": funder_agency_class,
                "keywords": keywords,
                "sponsor": sponsor,
                "collaborators": collaborators,
                "location_facility": location_facility,
                "country": country,
                "geo_point": geo_point,
                "first_post_date": first_post_date,
                "last_update_post_date": last_update_post_date
            })

    return pd.DataFrame(study_data)

