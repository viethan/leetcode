void reverse(char *s, int i, int j) {
    int temp;
    
    while (i < j) {
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        
        ++i; --j;
    }
}

char *rmExtraSpaces(char *s) {
    
    // removing leading spaces
    int i = 0, beginning;
    while (s[i] == ' ')
        i++;
    beginning = i;
    
    // remove trailing spaces
    i = strlen(s) - 1;
    while (s[i] == ' ')
        i--;
    s[i + 1] = NULL;
    
    // remove multiple spaces inbetween
    i = beginning;
    
    int j, k;
    while (s[i] != NULL) {
        if (s[i] == ' ' && s[i + 1] == ' ') {
            j = k = i + 1;
            while(s[j] == ' ')
                j++;
            while (s[j] != NULL)
                s[k++] = s[j++];
            s[k] = NULL;
        }
        i++;
    }
    
    
    return &s[beginning];
}

char * reverseWords(char * s){
    reverse(s, 0, strlen(s) - 1);
    s = rmExtraSpaces(s);
    
    int left, right;
    left = right = 0;
    
    while (right <= strlen(s)) {
        if (s[right] == ' ' || right == strlen(s)) {
            reverse(s, left, right - 1);
            left = right + 1;
        }
        right++;
    }
    
    return s;
}
