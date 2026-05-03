class Solution {
    void bfs(int row, int col, int[][] grid, int[][] distance) {
        int m = grid.length;
        int n = grid[0].length;
        var deque = new LinkedList<Pair<Integer, Integer>>();
        deque.add(new Pair<>(row, col));
        int d = 0;
        while (!deque.isEmpty()) {
            int l = deque.size();
            for (int k = 0; k < l; k++) {
                var coords = deque.removeFirst();
                int i = coords.getKey();
                int j = coords.getValue();
                distance[i][j] = d;
                if (i - 1 >= 0 && distance[i - 1][j] == Integer.MAX_VALUE && grid[i - 1][j] == 0) deque.add(new Pair<>(i - 1, j));
                if (i + 1 < m && distance[i + 1][j] == Integer.MAX_VALUE && grid[i + 1][j] == 0) deque.add(new Pair<>(i + 1, j));
                if (j - 1 >= 0 && distance[i][j - 1] == Integer.MAX_VALUE && grid[i][j - 1] == 0) deque.add(new Pair<>(i, j - 1));
                if (j + 1 < n && distance[i][j + 1] == Integer.MAX_VALUE && grid[i][j + 1] == 0) deque.add(new Pair<>(i, j + 1));
            }
            d++;
        }
    }
    public int shortestDistance(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] distance = new int[m][n];

        var deque = new LinkedList<Pair<Integer, Integer>>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int[][] dist = new int[m][n];
                    for (int r = 0; r < m; r++) Arrays.fill(dist[r], Integer.MAX_VALUE);
                    bfs(i, j, grid, dist);
                    for (int r = 0; r < m; r++) {
                        for (int c = 0; c < n; c++) {
                            if (Math.max(distance[r][c], dist[r][c]) < Integer.MAX_VALUE)
                                distance[r][c] += dist[r][c];
                            else
                                distance[r][c] = Integer.MAX_VALUE;
                        }
                    }
                }
            }
        }

        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0)
                    ans = Math.min(ans, distance[i][j]);
            }
        }

        return ans < Integer.MAX_VALUE ? ans : -1;
    }
}
