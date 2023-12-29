# Changelog
## [1.1.2](https://github.com/fugle-dev/fugle-trade-python/compare/1.1.0...1.1.1) -

### Fixed
  - 修正 recover_order_result 沒有正確將整股的qty轉換成int的問題
# Changelog
## [1.1.1](https://github.com/fugle-dev/fugle-trade-python/compare/1.1.0...1.1.1) -

### Fixed
  - 修改 function name get_order_result_by_date => get_order_results_by_date
## [1.1.0](https://github.com/fugle-dev/fugle-trade-python/compare/1.0.0...1.1.0) -

### Added
  - 增加可以用日期查詢委託回報的 function get_order_result_by_date

## [1.0.0](https://github.com/fugle-dev/fugle-trade-python/compare/0.5.2...1.0.0) -

### Breaking
  - fugle-trade-core 升級到 1.0.0, 修改委託回報 order_no, pre_order_no 行為

## [0.5.2](https://github.com/fugle-dev/fugle-trade-python/compare/0.5.1...0.5.2) -
### Fixed
  - fugle-trade-core 升級到 0.5.1, 修正 multi-thread 下單時候卡頓
  - 修改 websocket-client 版本需求限制

## [0.5.1](https://github.com/fugle-dev/fugle-trade-python/compare/0.5.0...0.5.1) -
### Fixed
  - 修正 on_close callback 的參數錯誤


## [0.5.0](https://github.com/fugle-dev/fugle-trade-python/compare/0.4.0...0.5.0) -
### Added
  - fugle-trade-core 升級到 0.5.0
  - 增加可以用日期查詢成交回報的 function get_transactions_by_date

## [0.4.0](https://github.com/fugle-dev/fugle-trade-python/compare/0.3.1...0.4.0) -
  - 許多修改 [MR_8](https://github.com/fugle-dev/fugle-trade-python/pull/8)
  - 改價可以同時改價格旗標
  - 增加查詢銀行餘額
  - 增加查詢交易狀態
  - 增加查詢市場是否開盤
  - const: Trade, 移除自動當沖
  - 改善找不到憑證檔案的錯誤訊息


## [0.3.1](https://github.com/fugle-dev/fugle-trade-python/compare/0.3.0...0.3.1) -

### Fixed

- 修正預約單 websocket parse 錯誤

## [0.3.0](https://github.com/fugle-dev/fugle-trade-python/compare/0.2.7...0.3.0) -

### Added

- add convert_ws_object from core and apply [MR_8](https://github.com/fugle-dev/fugle-trade-python/pull/8)


## [0.2.7](https://github.com/fugle-dev/fugle-trade-python/compare/0.2.6...0.2.7) -

### Added

- add: allow user to switch keyring backend  [MR 7](https://github.com/fugle-dev/fugle-trade-python/pull/7)

## [0.2.6](https://github.com/fugle-dev/fugle-trade-python/compare/0.2.5...0.2.6) -  21 June 2022

### Fixed

- fix: odd order cancel_order error [MR 4](https://github.com/fugle-dev/fugle-trade-python/pull/4)
- chore: use docstring for enum names [MR 3](https://github.com/fugle-dev/fugle-trade-python/pull/3)

## [0.2.5](https://github.com/fugle-dev/fugle-trade-python/compare/0.2.4...0.2.5) -  17 May 2022

### Added

- feat: mock fugle_trade_core and test sdk [MR 1](https://github.com/fugle-dev/fugle-trade-python/pull/1)

## 0.2.4
  Public release
