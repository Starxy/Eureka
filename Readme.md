# Artifact 卡组价格插件
- [x] api 接口
- [x] Steam商店价格获取
- [ ] 本地 DeckCode 编码
- [ ] 缓存图片描述
- [ ] 定期更新牌组信息
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
返回卡片单价和卡组总价

# 参照

- [ArtifactDeckCode](https://github.com/ValveSoftware/ArtifactDeckCode) 
