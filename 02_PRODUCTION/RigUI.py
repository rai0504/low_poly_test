import bpy

# Rig Controls
class RigControls(bpy.types.Panel):
    bl_label = "Rig Controls"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "posemode"
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        pose_bones = context.active_object.pose.bones
        try:
            selected_bones = [bone.name for bone in context.selected_pose_bones]
            selected_bones += [context.active_pose_bone.name]
        except (AttributeError, TypeError):
            return
    
        def isSelected(names):
        # return whether any of the named bones are selected
            if type(names) == list:
                for name in names:
                    if name in selected_bones:
                        return True
            elif names in selected_bones:
                return True
            return False
    
        # define the names we'll use for the bones and what controls to show when they're selected
        head = "C_headNneck"
        neck = "D_neck"
        if isSelected([head, neck]):
            layout.prop(pose_bones["C_headNneck"], '["isolate_head"]', slider=True)
            
        chest = "C_chest"
        spine = "C_spine"
        hips = "C_hips"
        torso = "C_torso"
        if isSelected([chest, spine, hips, torso]):
            layout.prop(pose_bones["C_torso"], '["pivot_slide"]', slider=True)
            
        shoulderr = "D_shoulder.R"
        uparmfkr = "CFK_upperarm.R"
        forearmfkr = "CFK_forearm.R"
        handfkr = "CFK_hand.R"
        if isSelected([shoulderr, uparmfkr, forearmfkr, handfkr]):
            layout.prop(pose_bones["CFK_upperarm.R"], '["isolate right arm"]', slider=True)
            
        handikr = "CIK_hand.R"
        elbowpoler = "C_elbow_target.R"
        if isSelected([shoulderr, uparmfkr, forearmfkr, handfkr, handikr, elbowpoler]):
            layout.prop(pose_bones["CIK_hand.R"], '["fk_ik right arm"]', slider=True)
            
        shoulderl = "D_shoulder.L"
        uparmfkl = "CFK_upperarm.L"
        forearmfkl = "CFK_forearm.L"
        handfkl = "CFK_hand.L"
        if isSelected([shoulderl, uparmfkl, forearmfkl, handfkl]):
            layout.prop(pose_bones["CFK_upperarm.L"], '["isolate left arm"]', slider=True)
            
        handikl = "CIK_hand.L"
        elbowpolel = "C_elbow_target.L"
        if isSelected([shoulderl, uparmfkl, forearmfkl, handfkl, handikl, elbowpolel]):
            layout.prop(pose_bones["CIK_hand.L"], '["fk_ik left arm"]', slider=True)
        
        thighfkr = "CFK_thigh.R"
        shinfkr = "CFK_shin.R"
        footfkr = "CFK_foot.R"
        toefkr = "CFK_toe.R"
        if isSelected([thighfkr, shinfkr, footfkr, toefkr]):
            layout.prop(pose_bones["CFK_thigh.R"], '["isolate right leg"]', slider=True)
        
        footikr = "CIK_foot.R"
        toeikr = "CIK_toe.R"
        footrollr = "C_foot_roll.R"
        kneepoler = "CIK_knee_target.R"
        if isSelected([thighfkr, shinfkr, footfkr, toefkr, footikr, toeikr,footrollr, kneepoler]):
            layout.prop(pose_bones["CIK_foot.R"], '["fk_ik right leg"]', slider=True)
        
        thighfkl = "CFK_thigh.L"
        shinfkl = "CFK_shin.L"
        footfkl = "CFK_foot.L"
        toefkl = "CFK_toe.L"
        if isSelected([thighfkl, shinfkl, footfkl, toefkl]):
            layout.prop(pose_bones["CFK_thigh.L"], '["isolate left leg"]', slider=True)
            
        footikl = "CIK_foot.L"
        toeikl = "CIK_toe.L"
        footrolll = "C_foot_roll.L"
        kneepolel = "CIK_knee_target.L"
        if isSelected([thighfkl, shinfkl, footfkl, toefkl, footikl, toeikl,footrolll, kneepolel]):
            layout.prop(pose_bones["CIK_foot.L"], '["fk_ik left leg"]', slider=True)
            
        eyetarget = "C_eye_target"
        if isSelected([head, eyetarget]):
            layout.prop(pose_bones["C_eye_target"], '["follow head"]', slider=True)
            
        eyebrowr = "C_eyebrow.R"
        if isSelected([eyebrowr]):
            layout.prop(pose_bones["C_eyebrow.R"], '["mad.R"]', slider=True)
            layout.prop(pose_bones["C_eyebrow.R"], '["sad.R"]', slider=True)
            layout.prop(pose_bones["C_eyebrow.R"], '["surprise.R"]', slider=True)
            
        eyebrowl = "C_eyebrow.L"
        if isSelected([eyebrowl]):
            layout.prop(pose_bones["C_eyebrow.L"], '["mad.L"]', slider=True)
            layout.prop(pose_bones["C_eyebrow.L"], '["sad.L"]', slider=True)
            layout.prop(pose_bones["C_eyebrow.L"], '["surprise.L"]', slider=True)

# Rig Layers
class RigLayers(bpy.types.Panel):
    bl_label = "Rig Layers"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "posemode"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=0, toggle=True, text='head')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=1, toggle=True, text='eyes')
        row.prop(context.active_object.data, 'layers', index=17, toggle=True, text='face')
        row.prop(context.active_object.data, 'layers', index=7, toggle=True, text='hair')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=16, toggle=True, text='torso')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=8, toggle=True, text='coat main')
        row.prop(context.active_object.data, 'layers', index=24, toggle=True, text='coat fine')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=2, toggle=True, text='fk arms.R')
        row.prop(context.active_object.data, 'layers', index=3, toggle=True, text='fk arms.L')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=18, toggle=True, text='ik arms.R')
        row.prop(context.active_object.data, 'layers', index=19, toggle=True, text='ik arms.L')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=4, toggle=True, text='fingers main')
        row.prop(context.active_object.data, 'layers', index=20, toggle=True, text='fingers fine')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=5, toggle=True, text='fk legs.R')
        row.prop(context.active_object.data, 'layers', index=6, toggle=True, text='fk legs.L')
        
        row = col.row()
        row.prop(context.active_object.data, 'layers', index=21, toggle=True, text='ik legs.R')
        row.prop(context.active_object.data, 'layers', index=22, toggle=True, text='ik legs.L')

        row = col.row()
        row.prop(context.active_object.data, 'layers', index=23, toggle=True, text='ROOT') 
        
        
        
bpy.utils.register_class(RigControls)
bpy.utils.register_class(RigLayers)