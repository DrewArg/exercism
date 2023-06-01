import java.util.regex.Matcher;
import java.util.regex.Pattern;

class SqueakyClean {
    static String clean(String identifier) {
        identifier.replaceAll(" ", "_");
        Pattern regex = Pattern.compile("(<start>\\w+)(<control>\\\\\\d+)(<end>\\w+)");
        Matcher match = regex.matcher(identifier);


        return "";
    }
}
