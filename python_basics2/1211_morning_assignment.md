# 12/11 morning assignment

## 1. Fork & Pull Request

### (1) Fork

**`Fork`**는 타인의 Github repository에서 내가 어떤 부분을 수정하거나 추가 기능을 넣고 싶을 때 해당 respository를 내 Github repository로 그대로 복제하는 기능이다. fork한 저장소는 원본(타인의 github repository)와 연결되어 있다. 여기서 **`연결 되어 있다`**는 의미는 original repository에 어떤 변화가 생기면(새로운 commit) 이는 그대로 forked된 repository로 반영할 수 있다. 이 때 fetch나 rebase의 과정이 필요하다.

### (2) Pull Request

**`Fork`** 과정을 거친 후 original repository에 변경 사항을 적용하고 싶으면 해당 저장소에 pull request를 해야한다. pull request가 original repository의 관리자로 부터 승인 되었으면 내가 만든 코드가 commit, merge되어 original 에 반영된다. pull request 하기 전까지는 내 Github 에 있는 forked repository에만 change가 적용된다.

> 즉 Repository에 권한이 없는 사용자가 저장소를 fork하고 fork한 자신의 저장소에 변경 사항을 적용한 후 Push한다. 이 후 원래 저장소(original repository)에 내 저장소에 있는 브랜치를 Pull Request 한다. 내가 만든 코드가 관리자로부터 승인이 되면 해당 저장소에 Merge 된다.



## 2. Pull 상황에서의 Conflict

**Git 충돌 (refusing to merge unrelated histories) 해결 : merge**

이 방법은 서로 다른 코드간의 충돌 발생 시, 충돌되는 두 코드 중 하나를 선택해서 이용하는 방법이 되겠습니다.

```
$ git commit -m "Resolve Conflict" 
```



**Git 충돌 (refusing to merge unrelated histories) 해결 : stash**

위 방법 말고도 **stash** 라는 해결방법 또한 존재합니다. stash는 '책갈피' 개념으로 생각하면 되는 개념으로서, 지금의 코드를 만들어내긴 했는데 뭔가 오류가 생기게 됩니다. 하지만 그렇다고 코드를 날려버리기엔 아까울 때, **백업 및 책갈피 개념**으로서 이 명령어를 쓰면 딱 좋을겁니다.

