# coding: utf-8
import os
import shutil


thu_muc_cha = os.path.abspath('..')
duong_dan_nen = os.path.join(
        thu_muc_cha,
        'profile_moi',
        )
ten_moi = os.path.join(
        thu_muc_cha,
        'profile_moi_nen'
        )
shutil.make_archive(ten_moi, "zip", duong_dan_nen)
