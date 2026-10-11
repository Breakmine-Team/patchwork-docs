import re

def on_page_markdown(markdown, page, config, files):
    pattern = r'\[\|(.*?)\|\]'
    
    def replace_badge(match):
        parts = match.group(1).split('|')
        
        # 3 parts: [|Icon|Label|Value|] OR [|Icon||Value|]
        if len(parts) == 3:
            icon_name = parts[0].strip()
            label = parts[1].strip()
            value = parts[2].strip()
            
            icon_element = f'<span class="p-badge-icon">:{icon_name}:</span>'
            # Only generate the label span if there is actual text provided
            label_element = f'<span class="p-badge-label">{label}</span>' if label else ''
            
        # 2 parts: [|Label|Value|]
        elif len(parts) == 2:
            icon_element = ''
            label_element = f'<span class="p-badge-label">{parts[0].strip()}</span>'
            value = parts[1].strip()
        else:
            return match.group(0)

        return (
            f'<span class="p-badge-container">'
            f'{icon_element}'
            f'{label_element}'
            f'<span class="p-badge-value">{value}</span>'
            f'</span>'
        )
        
    return re.sub(pattern, replace_badge, markdown)
