import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class LogLevels {

    public static String message(String logLine) {
        Pattern regex = Pattern.compile("(\\[)(\\w*)(\\]\\:)(\\s+)(^\\t)?(.*[^\\s])");
        Matcher match = regex.matcher(logLine);
        if (match.find()) {
            return match.group(6);
        } else {
            return "not found";
        }
    }

    public static String logLevel(String logLine) {
        Pattern regex = Pattern.compile("(\\[)(\\w*)(\\]\\:)(\\s)(\\w+)\\4(\\w+)");
        Matcher match = regex.matcher(logLine);
        if (match.find()) {
            return match.group(2).toLowerCase();
        } else {
            return "not found";
        }

    }

    public static String reformat(String logLine) {
        Pattern regex = Pattern.compile("(\\[)(\\w*)(\\]\\:)(\\s*)?(\\s\\w+)(\\s\\w+)(\\s\\w+)?");
        Matcher match = regex.matcher(logLine);

        if (match.find()) {

            String group5 = match.group(5).replaceAll(" ", "");
            String group6 = match.group(6);
            String group7 = match.group(7) == null ? "" : match.group(7);

            return group5 + group6 + group7 + " ("
                    + match.group(2).toLowerCase() + ")";

        } else {
            return "not found";
        }
    }
}
