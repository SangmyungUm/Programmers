class Solution {
    public String solution(String rsp) {
        String answer = "";
        System.out.println(rsp.charAt(0));
        
        for(int i = 0 ; i < rsp.length() ; i++){
            char temp = rsp.charAt(i);
            String tem2 = Character.toString(temp);
            if (tem2.equals("2")){
                answer += "0";
            }else if(tem2.equals("0")){
                answer += "5";
            }else if(tem2.equals("5")){
                answer += "2";
            }
        }
        return answer;
    }
}