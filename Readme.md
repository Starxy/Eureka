# Artifact 卡组价格查询
- [x] api 接口
- [x] Steam商店价格获取
- [ ] 本地 DeckCode 编码
    - [x] 本地 DeckDecode 编码
    - [ ] 本地 DeckEncode 编码
- [ ] 缓存图片描述
- [x] 定期更新牌组信息
- [ ] 前端

# 使用
`Config.py` 修改Redis相应地址端口
```
python3 Run.py
```

# Api接口
```
/code/<ArtifactDeckCode>
```
# 示例
单机勿压
```
ddns.starxy.cc:5051/code/
```
返回卡片单价和卡组总价

# 参照

- [ArtifactDeckCode](https://github.com/ValveSoftware/ArtifactDeckCode) 
