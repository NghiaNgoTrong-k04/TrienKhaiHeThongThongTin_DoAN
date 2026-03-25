# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
#1. TABLE HOC PHAN
class hoc_phan(osv.osv):
    _name='hoc.phan'
    _columns={
    'maHocPhan':fields.char('Ma Hoc Phan',size=45,required = True),
    'tenMonHoc':fields.char('Ten Mon Hoc',size = 45,required= True),
    'soTinChi':fields.integer('So Tin Chi',required=True),
    'tien_quyet_ids':fields.many2many('hoc.phan','mon_hoc_tien_quyet_rel','hp_id','hp_tq_id','Mon Tien Quyet'),

    }
    
   
#2. TABLE LOP HOC
class lop_hoc(osv.osv):
    _name='lop.hoc'
    _columns = {
    'maLop':fields.char('Ma Lop',size = 45, required= True),
    'tenHocPhan':fields.char('Ten Hoc Phan ( Mo Rong)', size = 45),
    'giangVien':fields.char('Giang Vien', size = 45, required = True),
    'ngayBatDau':fields.datetime('Ngay Bat Dau', required = True),
    'ngayKetThuc':fields.datetime('Ngay Ket Thuc', required = True),
    'ghiChu':fields.char('Ghi Chu'),
    #RELATIONSHIP
    'hoc_phan_id':fields.many2one('hoc.phan','Thuoc Hoc Phan',required = True),
    }
    
#3. TABLE DANG KY
class dang_ky(osv.osv):
    _name='dang.ky'
    _columns={
    'maDangKy':fields.char('Ma Dang Ky', size = 45, readonly = True),
    'ngayDangKy':fields.datetime('Ngay Gio Dang Ky'),
    'user_id':fields.many2one('res.users','Sinh Vien Dang Ky'), #Connect voi tk he thong
    'trangThai':fields.selection([('0','Nhap'),('1','Xac Nhan')],'Trang Thai'),
    'lop_hoc_ids':fields.many2many('lop.hoc','dang_ky_chi_tiet_rel','dk_id','lop_id','Danh Sach Lop Chon'),
    }
    
    _defaults = {
    'trangThai':'0', #Mac dinh la Nhap
    'ngayDangKy':fields.datetime.now, #Tu dong lay Time hien tai
    }