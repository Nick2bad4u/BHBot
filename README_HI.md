# BHBot 

Brawlhalla के लिए गोल्ड/XP फार्मिंग बॉट 

भारी रूप से [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ) 

### ------ -------------------------------------------------- ----------- 

### बॉट सक्रिय रूप से रखरखाव के लिए वापस आ गया है! 
###### बॉट को बनाए रखने या नई सुविधाएं जोड़ने में सहायता के लिए [डिस्कॉर्ड](https://discord.gg/2HDmuqqq9p "डिस्कॉर्ड") से जुड़ें! 

### -------------------------------------------------- -------------------- 

**चेतावनी:** सॉफ्टवेयर मूल रूप से निजी उपयोग के लिए विकसित किया गया था। 
हालाँकि इसे इसके लिए डिज़ाइन नहीं किया गया है, फिर भी यह संभावित रूप से अप्रत्याशित परिणामों का कारण बन सकता है, जिसमें इन-गेम मुद्राओं का उपयोग करके मल्लहल्ला के भीतर लेनदेन का निष्पादन भी शामिल है। 

**डेवलपर्स इस सॉफ़्टवेयर के उपयोग से होने वाले किसी भी नुकसान के लिए सभी उत्तरदायित्व से इनकार करता है। यह सलाह दी जाती है कि सावधानी से आगे बढ़ें और सॉफ़्टवेयर का उपयोग अपने विवेक से करें। ** 

(बॉट का 4/18/2024 तक बिना किसी समस्या के 3,000 घंटों से अधिक समय तक कई लोगों द्वारा परीक्षण किया गया है) 

# इंस्टालेशन 
नवीनतम रिलीज़ को हमेशा डाउनलोड किया जा सकता है [यहाँ से ](https://github.com/Nick2Bad4u/BHBot/releases) 

# विशेषताएं 

- पूरी तरह से पृष्ठभूमि में काम करता है 
- आपको परेशान न करने के लिए सीधे Brawlhalla पर इनपुट भेजता है 
- स्वचालित रूप से गेम लॉन्च करता है 
- स्वचालित रूप से लॉबी बनाता/सेट करता है 
- स्वचालित रूप से चुनता/बदलता है चरित्र और खेल की अवधि 
- स्वचालित रूप से एक्सपी सीमा का पता लगाता है और रीसेट करता है 
- कस्टम मोड का समर्थन करता है 
- कस्टम भाषाओं का समर्थन करता है 
- यहां तक ​​कि कस्टम फ़ॉन्ट का भी समर्थन करता है 
- ~~आपको कॉफी बनाता है~~ (अभी केवल चाय समर्थित है) 

# उपयोग 
- प्रक्रिया को सहज बनाने के लिए डिज़ाइन किया गया है। बस "सेटिंग्स" बटन पर क्लिक करके आवश्यक सेटिंग्स चुनें 
- एक बार सेटिंग्स सहेजे जाने के बाद, "स्टार्ट" बटन पर क्लिक करके प्रोग्राम शुरू करें 

# सीमाएं 
- बॉट को हां पर सेट करने के लिए "संक्षिप्त क्रॉसओवर" की आवश्यकता होती है। यदि आपको लगता है कि इसे स्वचालित रूप से ऐसा सेट करना चाहिए, तो कृपया [एक मुद्दा खोलें](https://github.com/nick2Bad4u/bhbot/issues) 
- बॉट को इनगेम भाषा को अंग्रेजी में सेट करने की आवश्यकता है। यदि आपको लगता है कि इसे स्वचालित रूप से ऐसा सेट करना चाहिए, तो कृपया [एक मुद्दा खोलें](https://github.com/nick2Bad4u/bhbot/issues) 

# तकनीकी अवलोकन 
- अंतर्निहित कोड हमेशा किसी के भी समीक्षा के लिए उपलब्ध है। 
- अनिवार्य रूप से, बॉट ब्रॉलहल्ला विंडो पर सीधे इनपुट प्रसारित करने के लिए विंडोज सेंडमैसेज एपीआई का उपयोग करता है। यह स्थितियों को समझने और किसी भी समय उचित कार्रवाई निर्धारित करने के लिए पिक्सेल पहचान का उपयोग करता है।

- BrawlhallaBot क्लास का सीधे उपयोग किया जा सकता है या आप इसके लिए एक कस्टम रैपर विकसित कर सकते हैं। इसे स्वतंत्र रूप से संचालित करने के लिए डिज़ाइन किया गया है, जिसमें gui.py केवल PySimpleGUI का उपयोग करके एक ग्राफिकल रैपर के रूप में कार्य करता है।