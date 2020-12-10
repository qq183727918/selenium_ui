# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/10 13:25
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : warehousereceipt.py
# @Software : PyCharm

import pymysql


def select_test():
    """
    id                               '主键'
    purchase_sn                      '采购单号',
    order_type                       '订单类型(0“样品订单”、1“赠品订单”，2“系统订单”，3“配件订单”，4“FBA订单”,5“额外加货订单”)',
    bill_source                      '单据来源(0"系统创建",1"手动创建")',
    purchase_status                  '采购单状态(0:初始状态，1:待厂商确认，2:拒单总裁审批，3:拒单完成，4:待付款，5:待发货，6:待收货，7:待入库，8:部分完成，9:待财务二审，10:二审完成，11:已完成)',
    group_id                         '小组id',
    buyer                            '采购员',
    domestic_warehouse_id            '国内收货仓库id',
    domestic_address                 '国内仓库地址',
    overseas_warehouse_id            '海外收货仓库id',
    estimated_domestic_arrival_date  '国内预计到货日期',
    estimated_overseas_arrival_date  '海外预计到货日期',
    estimated_loading_date           '预计装柜日期',
    domestic_required_arrival_date   '国内要求到达日期',
    domestic_required_delivery_date  '国内要求发货日期',
    is_freeze                        '是否冻结(0否，1是)',
    reconciliation_purchase_sn       '调仓采购确认单号',
    procurement_supplier_id          '供应商id',
    is_early_arrival_allowed         '是否允许早到货 0否 1是',
    is_tax                           '是否含税（0否·,1是）',
    is_visible                       '是否可见 1（拒单按钮） 2（驳回按钮）',
    created_time                     '创建日期',
    create_by                        '创建人',
    update_time                      '更新时间',
    update_by                        '更新人',
    is_delete                        '是否删除 0未删除 1已删除'
    """
    # 创建连接对象
    con = pymysql.connect(host='47.103.124.72', user='vevor', password='RNjIEP8q0e^pbQS$', database='scp', port=3306,
                          charset='utf8')
    # 获取游标cursor
    cur = con.cursor()
    # 执行数据库命令
    sql = 'select * from procurement_purchase_order  where id =2'
    cur.execute(sql)
    # # 执行sql
    # con.commit()
    # 获取查询结果集
    rs = cur.fetchall()
    # 关闭连接
    con.close()

    print(rs)


select_test()
