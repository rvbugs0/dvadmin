import { request } from '@/api/service'
export const urlPrefix = '/api/system/weatherinfo/'

/**
 * 列表查询
 */

export function GetList () {
  return request({
    url: urlPrefix + 'all_records/',
    method: 'get',
  })
}
