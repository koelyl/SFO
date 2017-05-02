
# coding: utf-8

DROP_COLS = ["*RESPNUM","CCGID", "RUNID", "DAY", "INTDATE", "EGYPTAIR", "SAQ", "DEST CODE", "AIRLINE CODE", "STRATA", "PEAK", "GATE", "METHOD", "FLIGHT", "LANG", "WEIGHT", "FLIGHT", "DESTGEO","Q3GETTO1", "Q3GETTO2", "Q3GETTO3", "Q3PARK", "Q8COM", "Q8COM2", "Q8COM3", "Q8COM4", "Q8COM5", "Q9COM", "Q9COM2", "Q9COM3", "Q10COM1", "Q10COM2", "Q10COM3", "Q12PRECOM1", "Q12PRECOM2", "Q12PRECOM3", "Q15COM1", "Q15COM2", "Q15COM3", "ARRTIME", "DEPTIME", "HOME"]

COLUMN_NAMES = {'BAREA': 'Trav_Boarding_area', 'AIRLINE': 'Trav_Airline', 'DESTINATION': 'Trav_Destination', 'DESTMARK': 'Trav_Dest_market_size', 'HOWLONG': 'Trav_Arr_to_dep_time', 'Q2PURP1': 'Trav_Travel_purpose', 'Q4BAGS': 'Has_checked_baggage','Q4STORE': 'Shopped_stores','Q4FOOD': 'Shopped_restaurant', 'Q4WIFI': 'Used_free_wifi','Q5TIMESFLOWN': 'Trav_Times_flownSFO', 'Q5FIRSTTIME': 'Trav_Is_first_SFO','Q6LONGUSE': 'Trav_yearsUsed_group', 'Q7ART': 'Rate_art', 'Q7FOOD': 'Rate_food', 'Q7STORE': 'Rate_stores', 'Q7SIGN': 'Rate_signs', 'Q7WALKWAYS': 'Rate_moving_walkways', 'Q7SCREENS': 'Rate_infoscreens', 'Q7INFODOWN': 'Rate_infobooth_LL', 'Q7INFOUP': 'Rate_infobooth_UL', 'Q7WIFI': 'Rate_free_wifi', 'Q7ROADS': 'Rate_roadsigns', 'Q7PARK': 'Rate_parking', 'Q7AIRTRAIN': 'Rate_airtrain', 'Q7LTPARKING': 'Rate_parking_shuttle', 'Q7RENTAL': 'Rate_rentacar', 'Q7ALL': 'Rate_SFO_overall', 'Q9BOARDING': 'Clean_boarding_area', 'Q9AIRTRAIN': 'Clean_airtrain', 'Q9RENTAL': 'Clean_rentacar', 'Q9FOOD': 'Clean_restaurant', 'Q9RESTROOM': 'Clean_restoom', 'Q9ALL': 'Clean_overall', 'Q10SAFE': 'How_safe_overall', 'Q11TSAPRE': 'Used_TSA_Precheck', 'Q13 COUNTY': 'Trav_County_of_origin', 'Q13GETRATE': 'Rate_trip_to_airport', 'Q14FIND': 'Ease_of_navigating_inside', 'Q14PASSTHRU': 'Ease_of_passing_security', 'Q15PROBLEM': 'Encountered_problems', 'Q16LIVE': 'Trav_How_local', 'Q17CITY': 'Trav_City', 'Q17COUNTRY': 'Trav_Country', 'Q18PET': 'Trav_with_pet', 'Q19AGE': 'Trav_age_group', 'Q20GENDER': 'Trav_gender', 'Q22FLY': 'Is_Frequent_flyer', 'Q23SJC': 'Used_SJC', 'Q23OAK': 'Used_OAK'}

CAT_COLS = ['Trav_Boarding_area', 'Trav_Airline', 'Trav_Destination', 'Trav_Dest_market_size',
                           'Trav_Travel_purpose', 'Has_checked_baggage', 'Shopped_stores', 'Shopped_restaurant',
                           'Trav_Times_flownSFO', 'Trav_Is_first_SFO', 'Trav_yearsUsed_group', 'Used_TSA_Precheck',
                           'Trav_County_of_origin', 'Encountered_problems', 'Trav_How_local','Trav_City', 
                           'Trav_Country', 'Trav_with_pet', 'Trav_age_group', 'Trav_gender', 'Is_Frequent_flyer', 'Used_free_wifi',
                           'Used_SJC','Used_OAK']


PERCENT_MISSING = .15


