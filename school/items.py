# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SchoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    c_school_id = scrapy.Field()
    c_data_code = scrapy.Field()
    c_type = scrapy.Field()
    c_school_type = scrapy.Field()
    c_school_nature = scrapy.Field()
    c_level = scrapy.Field()
    c_code_enroll = scrapy.Field()
    c_f985 = scrapy.Field()
    c_f211 = scrapy.Field()
    c_department = scrapy.Field()
    c_admissions = scrapy.Field()
    c_central = scrapy.Field()
    c_dual_class = scrapy.Field()
    c_is_seal = scrapy.Field()
    c_num_subject = scrapy.Field()
    c_num_master = scrapy.Field()
    c_num_doctor = scrapy.Field()
    c_num_academician = scrapy.Field()
    c_num_library = scrapy.Field()
    c_num_lab = scrapy.Field()
    c_province_id = scrapy.Field()
    c_city_id = scrapy.Field()
    c_county_id = scrapy.Field()
    c_is_ads = scrapy.Field()
    c_is_recruitment = scrapy.Field()
    c_create_date = scrapy.Field()
    c_area = scrapy.Field()
    c_old_name = scrapy.Field()
    c_status = scrapy.Field()
    c_add_id = scrapy.Field()
    c_update_id = scrapy.Field()
    c_ad_level = scrapy.Field()
    c_e_pc = scrapy.Field()
    c_e_app = scrapy.Field()
    c_ruanke_rank = scrapy.Field()
    c_colleges_level = scrapy.Field()
    c_doublehigh = scrapy.Field()
    c_wsl_rank = scrapy.Field()
    c_qs_rank = scrapy.Field()
    c_xyh_rank = scrapy.Field()
    c_is_sell = scrapy.Field()
    c_postcode = scrapy.Field()
    c_name = scrapy.Field()
    c_belong = scrapy.Field()
    c_short = scrapy.Field()
    c_single = scrapy.Field()
    c_logo = scrapy.Field()
    c_level_name = scrapy.Field()
    c_type_name = scrapy.Field()
    c_school_type_name = scrapy.Field()
    c_school_nature_name = scrapy.Field()
    c_dual_class_name = scrapy.Field()
    c_single_province = scrapy.Field()
    c_province_name = scrapy.Field()
    c_city_name = scrapy.Field()
    c_town_name = scrapy.Field()
    c_weiwangzhan = scrapy.Field()
    c_yjszs = scrapy.Field()
    c_xiaoyuan = scrapy.Field()
    c_email = scrapy.Field()
    c_school_email = scrapy.Field()
    c_address = scrapy.Field()
    c_site = scrapy.Field()
    c_school_site = scrapy.Field()
    c_phone = scrapy.Field()
    c_school_phone = scrapy.Field()
    c_content = scrapy.Field()
    t_add_time = scrapy.Field()
    t_update_time = scrapy.Field()

    pass

class SpecialItem(scrapy.Item):
    # define the fields for your item here like:
    c_url = scrapy.Field()
    c_limit_year = scrapy.Field()
    c_level2_name = scrapy.Field()
    i_special_id = scrapy.Field()
    c_degree = scrapy.Field()
    i_rank_type = scrapy.Field()
    i_view_week = scrapy.Field()
    i_view_total = scrapy.Field()
    c_level3_name = scrapy.Field()
    c_name = scrapy.Field()
    i_rank = scrapy.Field()
    i_rankall = scrapy.Field()
    c_id = scrapy.Field()
    c_spcode = scrapy.Field()
    i_level1 = scrapy.Field()
    i_level3 = scrapy.Field()
    c_level1_name = scrapy.Field()
    i_view_month = scrapy.Field()
    i_level2 = scrapy.Field()
    pass

class LineproItem(scrapy.Item):
    # define the fields for your item here like:
    c_id = scrapy.Field()
    i_average = scrapy.Field()
    c_local_batch_name = scrapy.Field()
    c_local_province_name = scrapy.Field()
    c_local_type_name = scrapy.Field()
    i_year = scrapy.Field()
    pass