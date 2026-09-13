class Solution {
    public int largestOverlap(int[][] img1, int[][] img2) {
        int n=img1.length;
        int maxOverlap=0;
        //Shift img1 by row shift
        for(int dr=-(n-1);dr<=n-1;dr++){
            //Shift image1 by column shift
            for(int dc=-(n-1);dc<=n-1;dc++){
                int count=0;
                //Check every cell of img1
                for(int i=0;i<n;i++){
                    for(int j=0;j<n;j++){
                        int ni=i+dr;
                        int nj=j+dc;

                        //Check if shifted position is inside img2
                        if(ni>=0 && ni<n && nj>=0 && nj<n){
                            if(img1[i][j]==1 && img2[ni][nj]==1){
                                count++;
                            }
                        }
                    }
                }
                maxOverlap=Math.max(maxOverlap,count);
            }
        }
        return maxOverlap;
    }
}