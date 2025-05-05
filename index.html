<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>알케인 구조이성질체 계산기</title>
  <style>
    body { font-family: sans-serif; padding: 20px; }
    input, button { font-size: 16px; padding: 5px; margin: 5px; }
    #result { margin-top: 15px; font-size: 18px; }
  </style>
</head>
<body>
  <h1>알케인 구조이성질체 계산기</h1>
  <label>탄소 개수 n 입력 (1 ≤ n ≤ 6): </label>
  <input type="number" id="carbonInput" min="1" max="6" />
  <button onclick="calculate()">계산</button>

  <div id="result"></div>

  <script>
    function calculate() {
      const n = parseInt(document.getElementById("carbonInput").value);
      if (isNaN(n) || n < 1 || n > 6) {
        alert("1 이상 6 이하의 정수를 입력하세요.");
        return;
      }

      const unique = new Set();
      generateTrees(n, [[]], 0, unique);
      document.getElementById("result").innerText =
        `C${n}H${2 * n + 2}의 구조이성질체 수: ${unique.size}`;
    }

    function generateTrees(n, nodeList, nextId, uniqueSet) {
      if (nextId === n) {
        if (isValidTree(nodeList)) {
          const canon = canonicalForm(nodeList);
          uniqueSet.add(canon);
        }
        return;
      }

      if (nextId === 0) {
        nodeList.push([]);
        generateTrees(n, nodeList, 1, uniqueSet);
        return;
      }

      for (let i = 0; i < nodeList.length; i++) {
        if (nodeList[i].length < 4) {
          const newList = deepCopy(nodeList);
          newList.push([]);
          newList[i].push(nextId);
          newList[nextId].push(i);
          generateTrees(n, newList, nextId + 1, uniqueSet);
        }
      }
    }

    function isValidTree(adj) {
      const n = adj.length;
      const visited = Array(n).fill(false);
      if (!dfs(adj, 0, -1, visited)) return false;
      return visited.every(v => v);
    }

    function dfs(adj, u, parent, visited) {
      visited[u] = true;
      for (const v of adj[u]) {
        if (v === parent) continue;
        if (visited[v]) return false;
        if (!dfs(adj, v, u, visited)) return false;
      }
      return true;
    }

    function canonicalForm(adj) {
      const visited = Array(adj.length).fill(false);
      return encode(adj, 0, visited);
    }

    function encode(adj, u, visited) {
      visited[u] = true;
      const children = [];
      for (const v of adj[u]) {
        if (!visited[v]) {
          children.push(encode(adj, v, visited));
        }
      }
      children.sort();
      return "(" + children.join("") + ")";
    }

    function deepCopy(adj) {
      return adj.map(list => list.slice());
    }
  </script>
</body>
</html>
