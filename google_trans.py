from googletrans import Translator

def translate_text(text, target_language):

    translator = Translator()
    language_codes = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Arabic": "ar",
    "Hindi": "hi",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Swedish": "sv",
    "Danish": "da",
    "Norwegian": "no",
    "Finnish": "fi",
    "Greek": "el",
    "Polish": "pl",
    "Turkish": "tr",
    "Czech": "cs",
    "Hungarian": "hu",
    "Romanian": "ro",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Malay": "ms",
    "Hebrew": "he",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Sanskrit": "sa",
    "Persian": "fa",
    "Bulgarian": "bg",
    "Croatian": "hr",
    "Estonian": "et",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Slovenian": "sl",
    "Slovak": "sk",
    "Ukrainian": "uk",
    "Serbian": "sr",
    "Macedonian": "mk",
    "Albanian": "sq",
    "Georgian": "ka",
    "Armenian": "hy",
    "Haitian Creole": "ht",
    "Bengali": "bn",
    "Swahili": "sw",
    "Tagalog": "tl",
    "Farsi": "fa",
    "Icelandic": "is",
    "Maltese": "mt",
    "Samoan": "sm",
    "Tahitian": "ty",
    "Tongan": "to",
    "Maori": "mi",
    "Fijian": "fj",
    "Hawaiian": "haw",
    "Esperanto": "eo",
    "Latin": "la",
    "Yiddish": "yi",
    "Afrikaans": "af",
    "Zulu": "zu",
    "Xhosa": "xh",
    "Swati": "ss",
    "Ndebele": "nd",
    "Sotho": "st",
    "Tswana": "tn",
    "Northern Sotho": "nso",
    "Venda": "ve",
    "Tsonga": "ts",
    "South African English": "en-za",
    "Mandarin Chinese": "zh-cmn",
    "Hokkien": "zh-min-nan",
    "Cantonese": "zh-yue",
}

    
    try:
        detected_lang = translator.detect(text).lang
        
        if target_language in language_codes:
            lang=language_codes[target_language]
            translated_text = translator.translate(text, src=detected_lang, dest=lang)
            return translated_text.text
    except Exception as e:
        print("Translation error:", e)
        return None
t=input("enter: ")
t_lang = input("enter the language in which you wanna to convert the text: ")
translate_text(t,t_lang)
