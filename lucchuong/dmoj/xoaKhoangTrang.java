package lucchuong.dmoj;

public class xoaKhoangTrang {
    public static String removeCharAt(String s, int pos) {
        return s.substring(0, pos) + s.substring(pos + 1);
    }
    public static void main(String[] args) {
        String s = "pham luc chuong luc";
        char c = 'c';
        System.out.println(s.replace("luc", "van"));
        // System.out.println(removeCharAt(s, 5).length());
    }
}