

class Pair {
    int first;
    int second;

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
}

class Solution {

    public void bfs(int row, int col, int[][] vis, char[][] grid) {

        int n = grid.length;
        int m = grid[0].length;

        Queue<Pair> q = new LinkedList<>();
        q.offer(new Pair(row, col));
        vis[row][col] = 1;

        // 4 Directions: Up, Right, Down, Left
        int[] dRow = {-1, 0, 1, 0};
        int[] dCol = {0, 1, 0, -1};

        while (!q.isEmpty()) {

            Pair curr = q.poll();

            int curRow = curr.first;
            int curCol = curr.second;

            for (int i = 0; i < 4; i++) {

                int newRow = curRow + dRow[i];
                int newCol = curCol + dCol[i];

                if (newRow >= 0 && newRow < n &&
                    newCol >= 0 && newCol < m &&
                    vis[newRow][newCol] == 0 &&
                    grid[newRow][newCol] == '1') {

                    vis[newRow][newCol] = 1;
                    q.offer(new Pair(newRow, newCol));
                }
            }
        }
    }

    public int numIslands(char[][] grid) {

        if (grid == null || grid.length == 0) {
            return 0;
        }

        int n = grid.length;
        int m = grid[0].length;

        int[][] vis = new int[n][m];
        int count = 0;

        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {

                if (grid[row][col] == '1' && vis[row][col] == 0) {
                    count++;
                    bfs(row, col, vis, grid);
                }
            }
        }

        return count;
    }
}