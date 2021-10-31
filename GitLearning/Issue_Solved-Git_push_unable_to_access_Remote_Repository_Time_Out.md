# git push -u origin master unable to access Remote Repository解决



发生致命错误 fatal: unable to access 'https://github.com/xiangxing98/HeadFirstPython.git/': Failed to connect to github.com port 443: Timed out

```bash
# fatal: unable to access 'https://github.com/xiangxing98/HeadFirstPython.git/': Failed to connect to github.com port 443: Timed out

git remote -v
### origin  https://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@github.com/xiangxing98/HeadFirstPython.git (fetch)
### origin  https://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@github.com/xiangxing98/HeadFirstPython.git (push)
### upstream        https://github.com/foxli180/HeadFirstPython.git (fetch)
### upstream        https://github.com/foxli180/HeadFirstPython.git (push)

# git@github.com:xiangxing98/HeadFirstPython.git

git remote rm origin
git remote add origin git@github.com:xiangxing98/HeadFirstPython.git
git push -u origin master
```

